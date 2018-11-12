function [abott1] = BottomAlbedo1(lam,wavelength,Bott1)

% this function compute the absorption value at the desired lamda via linear interpolation
 


for i = 1:length(wavelength)
    
    if (wavelength(i) == lam)
        
        abott1 = Bott1(i);
      
        break
        
    elseif (wavelength(i) > lam)
        
        % m coefficient
        ma = (Bott1(i)-Bott1(i-1))/(wavelength(i)-wavelength(i-1));
      
        
        % compute the absorption at the desired wavelength
        abott1 = Bott1(i-1) + ma*(lam - wavelength(i-1));
        
        break
        
    else
        
        % do nothing
        
    end
    
    
end
        
        
        
        
        
        