function [view_w,sun_w,rho_L]=Snell_law(view,sun)

%% Index of refrations (real)

n_air= 1;  % air index of refration (real part)
n_w= 1.33; % water index of refration (real part)

%% Angles from the water

% from deg to rad
view=view*(180/pi); % rad
sun=sun*(180/pi);   % rad
% angles from the water rad
view_w= asin((n_air/n_w)*sin(view));   % rad
sun_w= asin((n_air/n_w)*sin(sun));     % rad

% Fresnel Law

rho_L= (1/2)*abs(((sin(view-view_w)^2)/(sin(view+view_w)^2))+((tan(view-view_w)^2)/(tan(view+view_w)^2)));
end