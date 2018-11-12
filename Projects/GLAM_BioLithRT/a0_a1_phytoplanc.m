function [a0,a1] = a0_a1_phytoplanc(lam,lam_p,a0_p,a1_p)

% this function compute the absorption and scattering value at the desired
% lamda via linear interpolation

for i = 1:length(lam_p)
    
    if (lam_p(i) == lam)
        
        a0 = a0_p(i);
        a1 = a1_p(i);
        break
        
    elseif (lam_p(i) > lam)
        
        % m coefficient
        ma0 = (a0_p(i)-a0_p(i-1))/(lam_p(i)-lam_p(i-1));
        ma1 = (a1_p(i)-a1_p(i-1))/(lam_p(i)-lam_p(i-1));
        
        % compute the absorption and scattering at the desired wavelength
        a0 = a0_p(i-1) + ma0*(lam - lam_p(i-1));
        a1 = a1_p(i-1) + ma1*(lam - lam_p(i-1));
        break
        
    else
        
        % do nothing
        
    end
    
    
end
        
        
        
        
        
        