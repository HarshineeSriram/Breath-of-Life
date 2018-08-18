import Algorithmia
input = {
"image": "data://harshineesriram/Breath_of_Life/001.jpg"
}
client = Algorithmia.client('simeteidDT51gYrNDMZFBhJX0t/1')
algo = client.algo('deeplearning/ColorfulImageColorization/1.1.13')
print(algo.pipe(input).result)
