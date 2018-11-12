function [abott2] = BottomAlbedo2(lam,wavelength,Bott2)

% this function compute the absorption value at the desired lamda via linear interpolation
 


for i = 1:length(wavelength)
    
    if (wavelength(i) == lam)
        
        abott2 = Bott2(i);
      
        break
        
    elseif (wavelength(i) > lam)
        
        % m coefficient
        ma = (Bott2(i)-Bott2(i-1))/(wavelength(i)-wavelength(i-1));
      
        
        % compute the absorption at the desired wavelength
        abott2 = Bott2(i-1) + ma*(lam - wavelength(i-1));
        
        break
        
    else
        
        % do nothing
        
    end
    
    
end
        
        
        
        
        
        