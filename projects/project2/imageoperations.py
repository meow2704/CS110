#Omyaasree Balaji
#project2
#part 2


from PIL import Image
import math

def main():
    # for Windows users the path specify the path as "c:\\users\\alark1\\Pictures\\usfca.png"


    while True:
        print ("What would you like to choose?")
        print ("1. copy the image")
        print ("2. Flip the image")
        print ("3. decode a secret message")
        print ("4. grayscale the image")
        print ("5. rotate image counterclockwise")
        print ("6. swap corners of an image")
        print ("7. blur an image")
        print ("8. sharpen an image")
        print ("9. extract an edge from the image")
        print ("10.resize the image")
        print ("11. Exit the program")
        user_input = int(input("Enter your choice: "))

  
        if user_input == 1:
            input_Image = Image.open('usfca.png')
            image_Width, image_Height = input_Image.size
            copy_Image(input_Image, image_Width, image_Height)
            print ("your image has been saved as copy.png")
            
        elif user_input == 2:
            input_Image = Image.open('usfca.png')
            image_Width, image_Height = input_Image.size
            flipVertical(input_Image, image_Width, image_Height)
            print ("your image has been saved as verticalflip.png")
            
        elif user_input == 3:
            input_Image = Image.open("red-image.png")
            image_Width, image_Height = input_Image.size   
            findPattern(input_Image, image_Width, image_Height)
            print("your image has been saved as mystery-solved.png")

        elif user_input == 4:
            input_Image = Image.open('usfca.png')
            image_Width, image_Height = input_Image.size
            makeGrayscale(input_Image, image_Width, image_Height)
            print ("your image has been saved as grayscale.png")

        elif user_input == 5:
            inputImage = Image.open('usfca.png')
            imageWidth, imageHeight = inputImage.size
            rotate(inputImage, imageWidth, imageHeight)
            print ("your image has been saved as rotate.png")

        elif user_input == 6:
            inputImage = Image.open('usfca.png')
            imageWidth, imageHeight = inputImage.size
            swapCorners(inputImage,imageWidth,imageHeight)
            print ("your image has been saved as cornerswap.png")

        elif user_input == 7:
            image = Image.open("usfca.png")
            imageWidth,imageHeight = image.size
            blur(image,imageWidth,imageHeight)
            print ("your image has been saved as blurred.png")

        elif user_input == 8:
            image = Image.open("usf.jpg")
            imageWidth,imageHeight = image.size
            sharpenimage(image,imageWidth,imageHeight)
            print ("your image has been saved as sharpened.png")

        elif user_input == 9:
            image = Image.open("usfca.png")
            width, height = image.size
            edgedetection(image, width, height)
            print ("your image has been saved as sobel.png")

        elif user_input == 10:
            image = Image.open("usfca.png")
            width, height = image.size
            scaleLarger(image, width, height)
            print ("your image has been saved as scaled.png")

        elif user_input == 11:
            print ("exiting the program")
            break


        else:
            print ("Please enter a valid choice!!!")



# Creates a copy of an image given the image variable, its width, and height
def copy_Image(input_Image, image_Width, image_Height):
    copy_Image_Output = Image.new('RGB', (image_Width, image_Height), 'white')

    for i in range(image_Width):
        for j in range(image_Height):
            pixel_Colors = input_Image.getpixel((i, j))
            copy_Image_Output.putpixel((i, j), pixel_Colors)

    copy_Image_Output.save("copy.png")



def flipVertical(input_Image, image_Width, image_Height):
    flipped_image_output = Image.new('RGB',(image_Width, image_Height), 'white')

    for i in range (image_Width):
        for j in range(image_Height):
            if 0 <= j < image_Height:
                image_color = input_Image.getpixel((i, image_Height- j- 1))
                flipped_image_output.putpixel((i,j), image_color)
    flipped_image_output.save("verticalflip.png")



def findPattern(input_Image, image_Width, image_Height):
    secret_Image_Output = Image.new('RGB', (image_Width, image_Height), 'white')

    for i in range(image_Width):
        for j in range(image_Height):
            r, g, b = input_Image.getpixel((i, j))
            if r > g and r > b:
                r = 255
                g = 255
                b = 255

            secret_Image_Output.putpixel((i, j), (r, g, b))

    secret_Image_Output.save("mystery-solved.png")



def makeGrayscale(input_Image, image_Width, image_Height):
    gray_Image_Output = Image.new('RGB', (image_Width, image_Height), 'white')

    for i in range(image_Width):
        for j in range(image_Height):
            pixel_Colors = input_Image.getpixel((i, j))
            gray_value = int(0.3 * pixel_Colors[0] + 0.59 * pixel_Colors[1] + 0.11 * pixel_Colors[2])
            gray_scale_color = (gray_value, gray_value, gray_value)
            gray_Image_Output.putpixel((i, j), gray_scale_color)

    gray_Image_Output.save("grayscale.png")



def rotate(inputImage, imageWidth, imageHeight):

    newwidth = imageHeight
    newheight = imageWidth
    rotatedImage = Image.new('RGB', (newwidth, newheight), 'white')

    for i in range(newwidth):
        for j in range(newheight):
            pixelColors = inputImage.getpixel((newheight - j - 1, i))
            rotatedImage.putpixel((i, j), pixelColors)

    rotatedImage.save("rotate.png")



def swapCorners(inputImage,imageWidth,imageHeight):

    cornerWidth = int(imageWidth / 2)
    cornerHeight = int(imageHeight / 2) 
    swapOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')
    
    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            swapOutput.putpixel((i - cornerWidth, j - cornerHeight), pixelColors)

    swapOutput.save("cornerswap.png")



def blur(image,imageWidth,imageHeight):

    blurred_image =  Image.new('RGB', (imageWidth, imageHeight), 'white')
    width, height = image.size

    for x in range(width):
        for y in range(height):
            total_red = 0
            total_green = 0
            total_blue = 0

            for i in range(x - 1, x + 2):
                for j in range(y - 1 , y + 2):
                    if 0 <= i and i < width and 0 <= j and j< height:
                        pixel = image.getpixel((i, j))
                        red = pixel[0]
                        blue = pixel[2]
                        green = pixel[1]
                        total_red += red
                        total_green += green
                        total_blue += blue

            avg_red = total_red // 9
            avg_green = total_green // 9
            avg_blue = total_blue // 9

            blurred_image.putpixel((x, y), (avg_red, avg_green, avg_blue))

    blurred_image.save("blurred.png")



def sharpenimage(image,imageWidth,imageHeight):

    sharp_image = Image.new('RGB', (imageWidth, imageHeight), 'white')
    width, height = image.size

    for x in range (width):
        for y in range (height):
            total_red = 0
            total_green = 0
            total_blue = 0

            for i in range(x - 1, x + 2):
                for j in range(y - 1 , y + 2):
                    if 0 <= i and i < width and 0 <= j and j< height:
                        pixel = image.getpixel((i, j))
                        red = pixel[0]
                        blue = pixel[2]
                        green = pixel[1]
                        total_red += red
                        total_green += green
                        total_blue += blue

            avg_red = total_red // 9
            avg_green = total_green // 9
            avg_blue = total_blue // 9

            sharp_image.putpixel((x, y), (red + (red -avg_red), green + (green - avg_green), blue+ (blue-avg_blue)))

    sharp_image.save("sharped.png")



def edgedetection(image, width, height):
    sobel_image = Image.new('RGB', (width, height), 'white')

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            red = 0
            green = 0
            blue = 0 

            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    pixel = image.getpixel((i, j))
                    red += pixel[0]
                    blue += pixel[2]
                    green += pixel[1]

            GXr = [1*red, 0*red, -1*red]
            GXg = [2*green, 0*green, -2*green]
            GXb = [1*blue, 0*blue, -1*blue]
            GYr = [1*red, 2*red, 1*red]
            GYg = [0*green, 0*green, 0*green]
            GYb = [-1*blue, -2*blue, -1*blue]

            total_x = (GXr[0] + GXr[1] + GXr[2] ) + (GXg[0] + GXg[1] + GXg[2] ) + (GXb[0] + GXb[1] + GXb[2])
            total_y = (GYr[0] + GYr[1] + GYr[2] ) + (GYg[0] + GYg[1] + GYg[2] ) + (GYb[0] + GYb[1] + GYb[2])

            new_pixel = int(math.sqrt(total_x**2 + total_y**2))

            sobel_image.putpixel((x, y), (new_pixel, new_pixel, new_pixel))

    sobel_image.save("sobel.png")



def scaleLarger(image, width, height):
    factor = float(input("Enter the scaling factor: "))


    new_width = int(width * factor)
    new_height = int(height * factor)    

    large_image = Image.new('RGB', (new_width, new_height), 'white')

    for x in range(new_width):
        for y in range(new_height):
            or_width = int(x / factor)
            or_height = int(y / factor)
            pixel = image.getpixel((or_width, or_height))
            large_image.putpixel((x, y), pixel)

    large_image.save("scaled.png")

    print("Image scaled and saved as scaled.png")     


main()

