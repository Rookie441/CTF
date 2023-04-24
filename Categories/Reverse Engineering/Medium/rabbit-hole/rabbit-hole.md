## Rabbit Hole

[RabbitHole.zip](https://github.com/Rookie441/CTF/blob/main/Categories/Reverse%20Engineering/Medium/rabbit-hole/RabbitHole.zip)  

> This is an [Easter Egg mini challenge](https://www.csit-events.sg/easter-egg-challenge23) created by [Centre for Strategic Infocomm Technologies](https://www.csit.gov.sg/), CSIT.

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Reverse%20Engineering/Medium/rabbit-hole/images/csit.png)

> We have to find the Easter egg which contains the flag. We are given a zip file which contains an executable written in C#. We first explore what the application does before proceeding to decompile it.

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Reverse%20Engineering/Medium/rabbit-hole/images/game.png)

> By launching the executable, we can see a rabbit in a hole with the title containing the X and Y coordinates of our mouse pointer in real time.

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Reverse%20Engineering/Medium/rabbit-hole/images/fail.png)

> Clicking on a random point will give us the error that the egg is not here and that it has moved to another location. Thus, we can see that the objective of the game is to click a random point until we find the easter egg. So why don't we just write a script to try every coordinate? Of course that wouldn't work since the author would have thought of this to deter the bruteforce kiddies. Plus, we're here to learn about reverse engineering, and not just getting the flag.

> To analyze the executable, we first have to decompile it. A useful tool would be [jetbrains](https://www.jetbrains.com/decompiler/), which decompiles .NET assemblies to C#.

> After decompiling, we can see the `MainWindow` class along with its attributes and methods.

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Reverse%20Engineering/Medium/rabbit-hole/images/mainwindow.png)

> We can analyze each method as follows:

```csharp
// Import required namespaces
using System;
...

namespace RabbitHole
{
  public class MainWindow : Window, IComponentConnector
  {
    internal Grid LayoutRoot; // Represent main grid
    internal Image myImg; // Represent Easter egg image
    private bool _contentLoaded; // Boolean flag that tracks whether the window content has been loaded

    public MainWindow() => this.InitializeComponent();

    private void Image_MouseLeftButtonUp(object sender, MouseButtonEventArgs e)
    {
      // Decrypts a hidden image if the user clicks on the correct spot, and displays it
    }

    private void Window_MouseMove(object sender, MouseEventArgs e)
    {
      // Code for updating the window title with mouse coordinates
    }

    private byte[] bbb(byte[] d, string k)
    {
      // Private method that decrypts an image using a XOR cipher with a key passed as a string parameter.
    }

    public void InitializeComponent()
    {
      // Code for loading the XAML file that defines the window layout
    }

    void IComponentConnector.Connect(int connectionId, object target)
    {
      // Implementation of the IComponentConnector interface method that connects event handlers to UI elements
    }
  }
}
```

> We can further explore the main functionality of the application by looking deeper into `Image_MouseLeftButtonUp()` and writing comments as we go along

```csharp
private void Image_MouseLeftButtonUp(object sender, MouseButtonEventArgs e)
{
  Random random = new Random();
  // dynamically load and resources from the compiled assembly at runtime
  Assembly executingAssembly = Assembly.GetExecutingAssembly();
  // defining strings from Resources folder
  string name1 = "RabbitHole.Resources.aa.txt";
  string name2 = "RabbitHole.Resources.a.txt";
  string name3 = "RabbitHole.Resources.aaa.txt";
  // returns a Stream object representing the specified embedded resource and assign it to a string array
  string[] strArray1 = new StreamReader(executingAssembly.GetManifestResourceStream(name2)).ReadToEnd().Split(',');
  string[] strArray2 = new StreamReader(executingAssembly.GetManifestResourceStream(name3)).ReadToEnd().Split(',');
  // Get location of user's mouse pointer
  Point position = Mouse.GetPosition((IInputElement) this);
  Point point1 = new Point(position.X, position.Y);
  // exact location of the easter egg is randomly determined from a list of coordinates stored in the previously defined string arrays
  Point point2 = new Point(Convert.ToDouble(strArray1[random.Next(1, 15) % strArray1.Length]), Convert.ToDouble(strArray2[random.Next(1, 21) % strArray2.Length]));
  // getting a key by calling the cc() method
  string k = new c().cc();
  if (point1 == point2)
  {
    // obtain a stream to read the contents of the "RabbitHole.Resources.aa.txt" file, which is then processed by the bbb() method, where the previously obtained key, k, is passed as an argument.
    MemoryStream memoryStream = new MemoryStream(this.bbb(Convert.FromBase64String(new StreamReader(executingAssembly.GetManifestResourceStream(name1)).ReadToEnd()), k));
    // creating the image
    BitmapImage bitmapImage = new BitmapImage();
    bitmapImage.BeginInit();
    bitmapImage.StreamSource = (Stream) memoryStream;
    bitmapImage.EndInit();
    this.myImg.Source = (ImageSource) bitmapImage;
  }
  else
  {
    // show failure message
    int num = (int) MessageBox.Show("The egg is not here and has moved to a new location! Please try again.", string.Format("X={0}, Y={1}", (object) point1.X, (object) point1.Y), MessageBoxButton.OK, MessageBoxImage.Hand);
  }
}
```

> It seems that we have some text files inside the Resources folder. We can check that out.

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Reverse%20Engineering/Medium/rabbit-hole/images/resources.png)

> We can double click one of them to see its contents displayed.

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Reverse%20Engineering/Medium/rabbit-hole/images/atxt.png)

> We can also see the `cc()` and `bbb()` functions mentioned earlier.

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Reverse%20Engineering/Medium/rabbit-hole/images/cc.png)  
![image](https://github.com/Rookie441/CTF/blob/main/Categories/Reverse%20Engineering/Medium/rabbit-hole/images/bbb.png)

> The return value of `cc()` gives us the key which we will need to pass into our `bbb()` function. However, to run `cc()`, we will need to read the contents of `RabbitHole.Resources.1.txt` to `RabbitHole.Resources.10.txt`

> We can get the contents by saving resource to file as follows:

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Reverse%20Engineering/Medium/rabbit-hole/images/saveresource.png)

> In the program's `bbb()` function, the first argument takes in the contents of `name1`, which is `RabbitHole.Resources.aa.txt`, and then base64 decodes it. The second argument is the key, `k`, which we would have obtained by running `cc()` as discussed above.

> The `bbb()` method uses the key to perform an XOR operation on the contents of the `aa.txt` file and returns the decrypted contents as a byte array.

> Now that we have all the information we need, we can create a python script to include the relevant methods and successfully decrypt the image.

```python
import io
import base64
from PIL import Image

def bbb(d, k):
    length1 = len(d)
    length2 = len(k)
    numArray = bytearray(length1)
    for index in range(length1):
        numArray[index] = d[index] ^ ord(k[index % length2])
    return bytes(numArray)

def cc():
    k = ""
    for num in range(1, 11):
        filename = f"RabbitHole.Resources.{num}.txt"
        with open(filename, "r") as f:
            content = f.read()
        startIndex = num * 5 * 7 // 9
        k += content[startIndex:startIndex+4]
    return k

with open("RabbitHole.Resources.aa.txt", "rb") as f:
    encrypted_data = base64.b64decode(f.read())

decrypted_data = bbb(encrypted_data, cc())

img_stream = io.BytesIO(decrypted_data)
image = Image.open(img_stream)
image.show()
image.save("flag.png")
```

> The script and relevant resource files can be found [here](https://github.com/Rookie441/CTF/blob/main/Categories/Reverse%20Engineering/Medium/rabbit-hole/solver/)

> Running the script with the resources in the same directory gives us the hidden easter egg that also contains the flag.

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Reverse%20Engineering/Medium/rabbit-hole/images/flag.png)

> We can submit the flag for a special reward - A digital badge

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Reverse%20Engineering/Medium/rabbit-hole/images/solved.png)

`CSIT{RAB81T5_c@n_$wiM}`
