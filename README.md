# Bilinear Interpolation App

A Python GUI application for demonstrating and calculating bilinear interpolation on images and custom data points. This tool is useful for understanding how bilinear interpolation works in computer graphics, image processing, and data visualization.
(This is the final project for the Object-Oriented Analysis and Design course at the Egyptian Chinese University)

## Features

- **Image Loading**: Load and display images in various formats (PNG, JPG, JPEG, BMP, GIF)
- **Interactive Point Selection**: Click on loaded images to see interpolated RGB values
- **Manual Interpolation**: Calculate bilinear interpolation using custom points and RGB values
- **Real-time Visualization**: View interpolated colors and results in real-time
- **Detailed Output**: Display interpolation points, RGB values, and color swatches

## Requirements

- Python 3.6 or higher
- tkinter (usually comes with Python)
- PIL (Pillow)
- numpy

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Bilinear-Interpolation-App.git
cd Bilinear-Interpolation-App
```

2. Install required dependencies:
```bash
pip install Pillow numpy
```

Note: `tkinter` is typically included with Python installations. If you encounter issues, you may need to install it separately depending on your system.

## Usage

### Running the Application

```bash
python "Bilinear Interpolation App.py"
```

### Using the Application

#### 1. Image-based Interpolation

1. Click **"Load Image"** to select an image file
2. Once loaded, click anywhere on the image to see the interpolated RGB values at that point
3. The interpolation point coordinates and RGB values will be displayed in the text area
4. A color swatch showing the interpolated color will appear at the bottom

#### 2. Manual Interpolation

1. Fill in the four corner points in the format `x,y` (e.g., `0,0`)
2. Enter the corresponding RGB values for each point in the format `r,g,b` (e.g., `255,0,0`)
3. Specify the interpolation point where you want to calculate the color
4. Click **"Calculate"** to see the interpolated result

**Example Input:**
- Point 1: `0,0` with RGB: `255,0,0` (red)
- Point 2: `1,0` with RGB: `0,255,0` (green)
- Point 3: `0,1` with RGB: `0,0,255` (blue)
- Point 4: `1,1` with RGB: `255,255,0` (yellow)
- Interpolation Point: `0.5,0.5`

The app supports fraction inputs for precise calculations (e.g., `1/2,1/3`).

## How Bilinear Interpolation Works

Bilinear interpolation is a method for estimating values between known data points in a 2D grid. The algorithm:

1. Takes four corner points with known values
2. Performs linear interpolation in the x-direction between adjacent points
3. Performs linear interpolation in the y-direction between the results
4. Returns the interpolated value at the specified point

The formula used is:
```
f(x,y) = f(x1,y1)(x2-x)(y2-y) + f(x2,y1)(x-x1)(y2-y) + f(x1,y2)(x2-x)(y-y1) + f(x2,y2)(x-x1)(y-y1)
```

Where the area is normalized to unit size (x2-x1 = y2-y1 = 1).

## Application Structure

- **BilinearInterpolationApp**: Main application class
- **load_image()**: Handles image file loading and display
- **interpolate_image_point()**: Processes mouse clicks on images
- **interpolate_user_input()**: Handles manual interpolation calculations
- **bilinear_interpolation()**: Performs interpolation on loaded images
- **bilinear_interpolation_manual()**: Performs interpolation on user-defined points
- **display_point_and_rgb()**: Shows results in the text area
- **display_color()**: Shows color swatches of interpolated results

## Use Cases

- **Educational**: Understanding bilinear interpolation concepts
- **Image Processing**: Analyzing pixel interpolation in image scaling
- **Computer Graphics**: Learning texture mapping and filtering techniques
- **Data Visualization**: Exploring interpolation between discrete data points
- **Research**: Testing interpolation algorithms and results

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Troubleshooting

**Issue**: "No module named 'PIL'"
**Solution**: Install Pillow using `pip install Pillow`

**Issue**: "No module named 'tkinter'"
**Solution**: 
- On Ubuntu/Debian: `sudo apt-get install python3-tk`
- On macOS: tkinter should be included with Python
- On Windows: tkinter is typically included with Python

**Issue**: Image not loading
**Solution**: Ensure the image file is in a supported format (PNG, JPG, JPEG, BMP, GIF)

## Future Enhancements

- Support for different interpolation methods (bicubic, nearest neighbor)
- Batch processing for multiple points
- Export functionality for results
- Interactive grid visualization
- Animation of interpolation process

## Author

Mohamed Taha Khattab - mohamed.taha.khattab0@gmail.com
