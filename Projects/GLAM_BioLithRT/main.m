%--------------------------------------------------------------------------
% Mr. Enrico Schiassi - PhD Student, SIE, University of Arizona
%--------------------------------------------------------------------------
% 1. Remote sensing reflectance simulation given the wavelengts, water 
% component concentrations, and the input listed below 
%
% 2. Water component concentrations retrievial given the observed and the
% simulated remote sensing reflectance- constrained optimization framework
%--------------------------------------------------------------------------
%% 
clear ; clc; close all
%%
%--------------------------------------------------------------------------
% Input
%--------------------------------------------------------------------------
%% Global Variables
% Warnings: 
% - 1: the names must be consistent in the main and the correspondent functions
% - 2: the fit quantities are not part of the global variables
%
global g_size lambda type_Rrs_below zB type_case_water fA g_dd g_dsr g_dsa f_dd f_ds alpha view view_w sun sun_w rho_L P RH Hoz WV  Rrs_obs
%
%% Wavelength
% Enter the range of wavelenght of interest
% The range allowed is [400:1:700]'; [nm]
% The range must match the range used in the data set
%
FW_mode_only=0; % FW_mode_only=0 to do not consider forward mode only
%                 FW_mode_only=1 to consider forward mode only
%
switch FW_mode_only
    case 0
        load STA10_09.Rrs
        lambda= STA10_09(:,1);                 % [nm]
    case 1
        lambda=[400:1:700]';                  % [nm]
        %load MultispectralLand8bands.txt
        %lambda= MultispectralLand8bands(:,1); % [nm]
end
%
%% Remote sensig reflectance observed/measured [1/sr]
%
switch FW_mode_only
    case 0
        Rrs_obs=STA10_09(:,2); % [1/sr]
    case 1
        Rrs_obs= zeros(size(lambda));
end
%   
%% Case Water Selection
type_case_water=2; % 1=case-1 water; 2=case-2 water
%
%% Angles
% Enter the view (camera) and the sun angles [degrees]
view=eps;  % [deg]
sun=40;    % [deg]
%
%% Water component concentrations
% Enter the water component concentratios
C_ph = eps    ;                 % [mg/m^3]  Concentration of Phytoplankton
C_CDOM=0   ;                    % [mg/m^3]  Concentration of CDOM
C_X = 0 ;                       % [g/m^3]   Concetration of suspended matter
g_size_microm= 33.6;            % [µm]      Grain size, default 33.6 [µm]  
g_size=g_size_microm*10^(-6);   % [m]       Grain size in meter
%
%% Input for the Remote Sensing Reflectance [1/sr] 
% Water column contribution: select deep water or shallow water
type_Rrs_below=1; % 0=deep water; 1=shallow water
%
% Bottom depth 
zB=4.00; % [m] 
%
% areal fraction of bottom surface
fA0=0; % constant 
fA1=0; % sand
fA2=1; % sediment
fA3=0; % Chara contraria
fA4=0; % Potamogeton perfoliatus
fA5=0; % Potamogeton pectinatus
fA= [fA0,fA1,fA2,fA3,fA4,fA5];
%
% Irradiance intensities [1/sr]
g_dd=0.05; g_dsr=0; g_dsa=0;
%
% Intensities of light sources 
f_dd= 1; f_ds= 1;
%
% Angstrom exponent
alpha = 1.317;
%
% Atmospheric pressure 
P = 1013.25; % [mbar]
%
% Relative Humidity
RH = 0.60;
%
% Scale height for ozone
Hoz=0.300; % [cm]
%
% Scale height of the precipitable water in the atmosphere
WV=2.500; % [cm]
%
%% Fit quantities
% All the fit quantities must be compotents of the following vector, not
% part of the global variables
%
Fit= [C_ph, C_CDOM, C_X];
%--------------------------------------------------------------------------
%%
%--------------------------------------------------------------------------
% Output
%--------------------------------------------------------------------------
%% Geometry
% compute the view (camera) and sun angles in the water [rad]; and the Fresnel coeff
[view_w,sun_w, rho_L]=Snell_law(view,sun); 
%
%% Simulated remote sensing reflectance 
%
[Rrs0, Res0]= AOP_Rrs(Fit);
% % Remote sensing reflectance plot
% figure(1)
% plot(lambda,Rrs0); grid on
% %xlim([400 700])
% title('Remote sensing reflectnace')
% xlabel('wavelength[nm]')
% ylabel('Rrs [1/sr]')
%
%% Water component concentrations retrievial (constrained optimization framework)
%
% Linear Constraints: the water component concentrations are nonnegative (inquality const.)
%
% inequalities constraints
Aineq=-eye(size(Fit,2));
bineq=zeros(size(Fit))';
% equalities constraints
Aeq=[];
beq=[];
% bound constraints
lb=[]; % lower
ub=[]; % upper
%
% objective function -> Res = sum((Rrs_obs-Rrs).^2)
obj=@InvModeBioLithRT;
%
% solving linear constrained optimization problem
[Fitret,Res]=fmincon(obj,Fit,Aineq,bineq,Aeq,beq,lb,ub);
%
%% Simulated remote sensing reflectance w/ retrieved water component concentrations
%
[Rrs_fit, Res_fit]= AOP_Rrs(Fitret);
%--------------------------------------------------------------------------
%% Plots
%
% Remote sensing reflectance plot
figure(1)
plot(lambda,Rrs0, '*',lambda,Rrs_fit,'*',lambda,Rrs_obs, '*'); grid on
%xlim([400 700])
title('Remote sensing reflectnace')
xlabel('wavelength[nm]')
ylabel('Rrs [1/sr]')
legend ('Rrs guess', 'Rrs fit' , 'Rrs measured')
%xlim([400 700])
%ylim([0 0.1])
%--------------------------------------------------------------------------
%%








