# Basic Image Processing Algorithms
## Author: Fabrício G. M. de Carvalho, Ph.D.



Folder description:
* src/ : Source-code folder, which includes one subfolder for each image processing operation category
	* template_matching: Basic algorithm that matchs a template image i<sub>MxN</sub> to some image i<sub>OxP</sub>. It is supposed that M <=O and N<=P. The sum of absolute differences is used to choose the best matching position (x and y displacements).
	* image_signature: Basic image signature implementation used to solve image classification problem. In this example .bmp files are used.
	
	
To run the examples, first create a virtual environment, activate it and install all the dependencies with
```console
	pip install -r requirements.txt
```

	