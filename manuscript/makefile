help:
	@echo "Available makes:"
	@echo "figs - convert figures to TIF/CMYK"
	@echo "clean - remove unused files"

all:
	make figs
	make clean

# Convert and rename figures
figs:
	convert Fig/flops.png -colorspace CMYK -units PixelsPerInch Fig/Figure1.tiff
	convert Fig/synthetic-bodies.png -colorspace CMYK -units PixelsPerInch Fig/Figure2.tiff
	convert Fig/noise-free-data.png -colorspace CMYK -units PixelsPerInch Fig/Figure3.tiff
	convert Fig/stability-comparison.png -colorspace CMYK -units PixelsPerInch Fig/Figure4.tiff
	convert Fig/TOB20_residuals.png -colorspace CMYK -units PixelsPerInch Fig/Figure5.tiff
	convert Fig/TOB20_histograms.png -colorspace CMYK -units PixelsPerInch Fig/Figure6.tiff
	convert Fig/Brazil_map.png -colorspace CMYK -units PixelsPerInch Fig/Figure7.tiff
	convert Fig/carajas_data.png -colorspace CMYK -units PixelsPerInch Fig/Figure8.tiff
	convert Fig/carajas_grav_gradient.png -colorspace CMYK -units PixelsPerInch Fig/Figure9.tiff

# Remove unused files
clean:
	rm *.aux *.bbl *.blg *.log *.lof *.lot *.synctex.gz *.out
