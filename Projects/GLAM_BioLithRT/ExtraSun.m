function [Esun] = ExtraSun(lam,wavelength,extra)

% this function compute the absorption value at the desired lamda via linear interpolation
 


for i = 1:length(wavelength)
    
    if (wavelength(i) == lam)
        
        Esun = extra(i);
      
        break
        
    elseif (wavelength(i) > lam)
        
        % m coefficient
        ma = (extra(i)-extra(i-1))/(wavelength(i)-wavelength(i-1));
      
        
        % compute the absorption at the desired wavelength
        Esun = extra(i-1) + ma*(lam - wavelength(i-1));
        
        break
        
    else
        
        % do nothing
        
    end
    
    
end
        
        
        
        
        
        