function [abs_O3] = AbsO3(lam,wavelength,oz)

% this function compute the absorption value at the desired lamda via linear interpolation
 


for i = 1:length(wavelength)
    
    if (wavelength(i) == lam)
        
        abs_O3 = oz(i);
      
        break
        
    elseif (wavelength(i) > lam)
        
        % m coefficient
        ma = (oz(i)-oz(i-1))/(wavelength(i)-wavelength(i-1));
      
        
        % compute the absorption at the desired wavelength
        abs_O3 = oz(i-1) + ma*(lam - wavelength(i-1));
        
        break
        
    else
        
        % do nothing
        
    end
    
    
end
        
        
        
        
        
        