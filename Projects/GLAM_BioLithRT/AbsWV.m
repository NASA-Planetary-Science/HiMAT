function [abs_WV] = AbsWV(lam,wavelength,wv)

% this function compute the absorption value at the desired lamda via linear interpolation
 


for i = 1:length(wavelength)
    
    if (wavelength(i) == lam)
        
        abs_WV = wv(i);
      
        break
        
    elseif (wavelength(i) > lam)
        
        % m coefficient
        ma = (wv(i)-wv(i-1))/(wavelength(i)-wavelength(i-1));
      
        
        % compute the absorption at the desired wavelength
        abs_WV = wv(i-1) + ma*(lam - wavelength(i-1));
        
        break
        
    else
        
        % do nothing
        
    end
    
    
end
        
        
        
        
        
        