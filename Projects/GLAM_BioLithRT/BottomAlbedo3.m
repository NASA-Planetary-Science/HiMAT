function [abott3] = BottomAlbedo3(lam,wavelength,Bott3)

% this function compute the absorption value at the desired lamda via linear interpolation
 


for i = 1:length(wavelength)
    
    if (wavelength(i) == lam)
        
        abott3 = Bott3(i);
      
        break
        
    elseif (wavelength(i) > lam)
        
        % m coefficient
        ma = (Bott3(i)-Bott3(i-1))/(wavelength(i)-wavelength(i-1));
      
        
        % compute the absorption at the desired wavelength
        abott3 = Bott3(i-1) + ma*(lam - wavelength(i-1));
        
        break
        
    else
        
        % do nothing
        
    end
    
    
end
        
        
        
        
        
        