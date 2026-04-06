def convert_pil_to_numpy_array(image_path):
    # Load Image an open the image
    from PIL import Image

    image = Image.open(image_path)
    width = image.size[0]
    height = image.size[1] 

    image.thumbnail((500, 256) if (width > height) else (256, 500))  

    left_margin = (image.width - 224) / 2
    upper_margin = (image.height - 224) / 2     # fixed
    lower_margin = upper_margin + 224           # fixed
    right_margin = left_margin + 224

    # fixed and renamed so you do not overwrite image all the time - helps debugging
    # now this has 2 dimensions that are non-zero
    image_crop = image.crop((left_margin, upper_margin, right_margin, lower_margin))

    # normalize
    image_arr = np.asarray(image) / 255
    mean = np.mean(image_arr)
    std_dv = np.std( image_arr )
    image_arr = (image_arr - mean)/std_dv 

    return image_crop