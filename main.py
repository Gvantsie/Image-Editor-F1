from PIL import Image
from PIL import ImageFilter

with Image.open("bunny.jpg") as original_image:
    print("მოცემული ფოტოს მახასიათებლებია:")
    print("ზომა:", original_image.size)
    print("ფორმატი:", original_image.format)
    print("ფოტოს ტიპი:", original_image.mode)
    original_image.show()

    # გავხადოთ ფოტო შავ-თეთრი
    image_bw = original_image.convert("L")
    image_bw.save("bunny_bw.jpg")
    print("შეცვლილი მახასიათებელია:")
    print("ფოტოს ტიპი:", image_bw.mode)
    image_bw.show()

    # გავხადოთ ფოტო დაბურული
    image_blured = original_image.filter(ImageFilter.BLUR)
    image_blured.save("bunny_blurred.jpg")
    image_blured.show()

    # ამოტრიალება 180 გრადუსით
    image_up = original_image.transpose(Image.ROTATE_180)
    image_up.save("bunny_up.jpg")
    image_up.show()

    # სარკის ეფექტი
    image_mirror = original_image.transpose(Image.FLIP_LEFT_RIGHT)
    image_mirror.save("bunny_mirrored.jpg")
    image_mirror.show()
