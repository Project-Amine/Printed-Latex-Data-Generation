from pathlib import Path
from download_data_utils import _download_raw_dataset_from_list, ImageProcessor, _unpack_a_tar,  _unpack_tars, _normalize_latex_data, _clean_formulas, _generate_svg_images, _turn_svg_to_png
from configs import PrintedLatexDataConfig






'''

Module to Generate Printed LaTex data from KDDCup, Arxiv, Wikipedia and other sources.


The following Global Parameters for parsing formulas are set in download_data_utils.py
                MAX_FORMULA_LENGTH_in_Bytes = 1024,
                MIN_FORMULA_LENGTH_BYTES = 40,

'''



class Generate_Printed_Tex():
    '''
           Printed Tex Data Module Parameters:


            -- download_tex_dataset: if Set True/False downloads the dataset TODO: upgrade to choose source arxiv,wiki etc
            -- generate_tex_formulas: if set True will download and generate the whole thing by running self._prepare_data_on_file() in Repository
            -- max_label_length: only keep the labels of len < max_label_length in the dataframe
            -- number_tex_formulas_to_generate: currently when set <1001 =, only unpacks one .tar file  TODO: make this better
            -- generate_svg_images_from_tex:  generates svg images using MathJax
            -- generate_png_from_svg: if set True will use the generated svg images to produce png images.
            -- number_png_images_to_use_in_dataset: number of png images to be used for the model from pandas dataframe







           -- image_height:
           -- image_width:




           '''

    def __init__(self,
                download_tex_dataset = False,
                generate_tex_formulas= False,
                max_label_length = 128,
                number_tex_formulas_to_generate=150,
                generate_svg_images_from_tex = False,
                generate_png_from_svg = False,
                number_png_images_to_use_in_dataset=120,

                image_height = 64,
                image_width = 512,



                 ):


        self.download_tex_dataset = download_tex_dataset
        self.generate_tex_formulas = generate_tex_formulas
        self.max_output_label_length = max_label_length
        self.number_tex_formulas_to_generate = number_tex_formulas_to_generate
        self.generate_svg_images_from_tex = generate_svg_images_from_tex
        self.generate_png_images_from_svg = generate_png_from_svg
        self.number_png_images_to_use_in_dataset = number_png_images_to_use_in_dataset


        self.image_height = image_height
        self.image_width = image_width




        # Downloading formulas
        if self.download_tex_dataset == True:
            self.download_tex_formulas()

        # Generating normalized formulas
        if self.generate_tex_formulas == True:
            self.process_tex_formulas()

        if self.generate_svg_images_from_tex == True:
            self.generate_svg_from_tex()

        if self.generate_png_images_from_svg == True:
            self.generate_png_from_svg()

        # Downloads tars to Data/raw_data

    def download_tex_formulas(self, *args, **kwargs):
        _download_raw_dataset_from_list(PrintedLatexDataConfig.metadata["urls"],
                                        PrintedLatexDataConfig.CHROME_RAW_DATA_DIRNAME)


