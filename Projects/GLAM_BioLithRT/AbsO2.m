function [abs_O2] = AbsO2(lam,wavelength,oxy)

% this function compute the absorption value at the desired lamda via linear interpolation
 


for i = 1:length(wavelength)
    
    if (wavelength(i) == lam)
        
        abs_O2 = oxy(i);
      
        break
        
    elseif (wavelength(i) > lam)
        
        % m coefficient
        ma = (oxy(i)-oxy(i-1))/(wavelength(i)-wavelength(i-1));
      
        
        % compute the absorption at the desired wavelength
        abs_O2 = oxy(i-1) + ma*(lam - wavelength(i-1));
        
        break
        
    else
        
        % do nothing
        
    end
    
    
end
        
        
        
        
        
        