function [abott4] = BottomAlbedo4(lam,wavelength,Bott4)

% this function compute the absorption value at the desired lamda via linear interpolation
 


for i = 1:length(wavelength)
    
    if (wavelength(i) == lam)
        
        abott4 = Bott4(i);
      
        break
        
    elseif (wavelength(i) > lam)
        
        % m coefficient
        ma = (Bott4(i)-Bott4(i-1))/(wavelength(i)-wavelength(i-1));
      
        
        % compute the absorption at the desired wavelength
        abott4 = Bott4(i-1) + ma*(lam - wavelength(i-1));
        
        break
        
    else
        
        % do nothing
        
    end
    
    
end
        
        
        
        
        
        