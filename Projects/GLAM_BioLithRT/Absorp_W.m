function [absorp_W] = Absorp_W(lam,wavelength,absorpt_W)

% this function compute the absorption value at the desired lamda via linear interpolation
 


for i = 1:length(wavelength)
    
    if (wavelength(i) == lam)
        
        absorp_W = absorpt_W(i);
      
        break
        
    elseif (wavelength(i) > lam)
        
        % m coefficient
        ma = (absorpt_W(i)-absorpt_W(i-1))/(wavelength(i)-wavelength(i-1));
      
        
        % compute the absorption at the desired wavelength
        absorp_W = absorpt_W(i-1) + ma*(lam - wavelength(i-1));
        
        break
        
    else
        
        % do nothing
        
    end
    
    
end
        
        
        
        
        
        