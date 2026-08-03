from PIL import Image

image1 = Image.open("image1.jpg").convert("RGB")
image2 = Image.open("image2.jpg").convert("RGB")
image3 = Image.open("image3.jpg").convert("RGB")

image1.save(
    "output.pdf",
    save_all=True,
    append_images=[image2, image3]
)

print("PDF created successfully!")
