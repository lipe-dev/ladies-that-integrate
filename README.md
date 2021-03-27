# Ladies That Integrate

Made for [Ladies That UX Floripa](https://www.instagram.com/ladiesthatuxfln/?hl=en).

## Usage:

### Got Python?
Before anything, check if you have Python installed on your system.

Here is a [Guide in English](https://realpython.com/installing-python/)

And here are some in portuguese, for [Linux](https://python.org.br/instalacao-linux/), [Mac](https://python.org.br/instalacao-mac/), or [Windows](https://python.org.br/instalacao-windows/).

### Download & Install:
First, you need to download the program. You can do that:

- With Git, by running

```shell
git clone https://github.com/lipe-dev/ladies-that-integrate.git
```

- Regular download, by clicking the green "Code" button at the top, and then "Download as Zip"
- Unzip the folder using your favorite method

After you have obtained the application code, you need to open a terminal and navigate to its containing folder. Here are a few useful commands to help wit that:

```shell
# List the current folder contents by typing:
ls

# Open a folder with:
cd <folder name>
```

Many OSes offer an `Open in Terminal` context menu option when you right click inside a folder from its UI, you can also try that.

Now that you are inside the project folder, you need to install it. Run this command to do so:

```shell
# This tells the app pip (python's package manager) to install all dependencies listed in the txt file
pip install -r requirements.txt

# In case that doesn't work, try this:
pip3 install -r requirements.txt
```

### Running

Now go ahead and run it, while still in the same folder as before, run this command:

```shell
python main.py <key> <app>
```

- Replace **key** with your API Key from Air Table, looks like `key12345678900`
- Replace **app** with your App ID (a code that looks like `app123456789000`, you can see it in the API docs)

This is the default usage. It will:

- Get the table entries from Air Table
    - Those will be filtered, and only those that are `Status = pending` and with `Imagem = false (no checkmark)` will be loaded.
    - Assign a random background image to each job
    - Create the Job image with text over it
    - Save them to the `/output` folder of the program.
    - Update the Air Table, setting `Imagem` to `true (checkmark)`
    - Celebrate the completion!
    
You can also change this behavior sugin the following params:

```shell
# Process all images, even those that have already been processed before
-a OR --all-images

# Select the background image, defaults to random
-b OR --background-image {random|purple|black}

# Select where the images will be saved, defaults to /output
-o [output path] OR --output-directory [output path]
```

Examples:
- To reprocess all images, even those that already have the checkmark in the `Imagem` column:
```shell
python main.py <key> <app> -a
# OR
python main.py <key> <app> --all-images
```
- To force usage of the purple background instead of random:
```shell
python main.py <key> <app> -b purple
# OR
python main.py <key> <app> --background-image purple
```
- To save in a custom folder in your PC: (replace with your desired path)
```shell
python main.py <key> <app> -o /home/felipe/Downloads/
# OR
python main.py <key> <app> --output-directory /home/felipe/Downloads/
```
- You can mix and match them at will.
```shell
python main.py <key> <app> -a -b purple -o /home/felipe/Downloads/
# OR
python main.py <key> <app> --all-images --background-image purple --output-directory /home/felipe/Downloads/
```

## Contributing

If you have any code improvements, [open a new Pull Request](https://github.com/lipe-dev/ladies-that-integrate/pulls)

## Issues

Questions, suggestions, bugs, etc... [open a new issue](https://github.com/lipe-dev/ladies-that-integrate/issues)

## Contact

Feel free to reach out to me directly if you need. You can find me at:

- My website, [Lipe.Dev](https://lipe.dev)
- By email, [fe@lipe.dev](mailto://fe@lipe.dev)

## License

[MIT](https://mit-license.org/)

Copyright © 2021 [lipe-dev](https://lipe.dev)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.