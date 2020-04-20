%wczytanie obrazu .png
[img_wo, map, alpha] = imread('piorunMPO.png');
img = imshow(img_wo);
img.AlphaData = alpha;
hold on;
pause(2);
close;

%przeskalowanie obrazka x2 x4 x16 r�nymi metodami
resize(img_wo, alpha, 2, 'nearest');
resize(img_wo, alpha, 4, 'bilinear');
resize(img_wo, alpha, 16, 'bicubic');

%rotacja obrazka o 22.5 stopnia zgodnie ze wskaz�wkami zegara
img_wo = imrotate(img_wo, -22.5);
alpha = imrotate(alpha, -22.5);
img = imshow(img_wo);
img.AlphaData = alpha;
hold on;
pause(2);
close;

%przeskalowanie obrazka x2 x4 x16 r�nymi metodami
resize(img_wo, alpha, 2, 'bilinear');
resize(img_wo, alpha, 4, 'bicubic');
resize(img_wo, alpha, 16, 'nearest');

%funkcja skaluj�ca dany obrazek
function resize(img_wo, alpha, size, method)
    img_wo = imresize(img_wo, size, method);
    alpha = imresize(alpha, size, method);
    img = imshow(img_wo);
    img.AlphaData = alpha;
    hold on;
    pause(2);
    close;
end
