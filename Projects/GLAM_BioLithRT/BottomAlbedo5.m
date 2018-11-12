function [abott5] = BottomAlbedo5(lam,wavelength,Bott5)

% this function compute the absorption value at the desired lamda via linear interpolation
 


for i = 1:length(wavelength)
    
    if (wavelength(i) == lam)
        
        abott5 = Bott5(i);
      
        break
        
    elseif (wavelength(i) > lam)
        
        % m coefficient
        ma = (Bott5(i)-Bott5(i-1))/(wavelength(i)-wavelength(i-1));
      
        
        % compute the absorption at the desired wavelength
        abott5 = Bott5(i-1) + ma*(lam - wavelength(i-1));
        
        break
        
    else
        
        % do nothing
        
    end
    
    
end
        
        
        
        
        
        