from pathlib import Path



# TODO: need to document and rename all directories names



class PrintedLatexDataConfig:
    DATA_DIRNAME = Path(__file__).resolve()                         # gives the root directory
    CHROME_RAW_DATA_DIRNAME = DATA_DIRNAME / "Data" / "raw_data" / "chrome"
    UNPACKED_LATEX_RAW_DATA_DIRNAME = DATA_DIRNAME / "raw_data" / "latex"
    PROCESSED_DATA_FOLDER = DATA_DIRNAME / "processed_data"

    UNPROCESSED_FORMULA_FILENAME = PROCESSED_DATA_FOLDER / "not_normalized" / "formulas.txt"
    NORMALIZED_FORMULAS_DIR = PROCESSED_DATA_FOLDER / "normalized"

    FORMULAS_PATH_TMP = NORMALIZED_FORMULAS_DIR / "formulas.norm.txt.tmp"
    FORMULAS_PATH_NO_TMP = NORMALIZED_FORMULAS_DIR / "formulas.norm.txt"
    PNG_FINAL_FORMULAS = PROCESSED_DATA_FOLDER / "final_png_formulas.txt"
    PNG_IMAGES_NAMES_FILE = PROCESSED_DATA_FOLDER/'corresponding_png_images.txt'
    GENERATED_PNG_DIR_NAME = PROCESSED_DATA_FOLDER / "generated_png_images"
    PREPROCESS_FORMULAS_SCRIPT_PATH = DATA_DIRNAME / "preprocess_formulas.py"
    GENERATED_SVG_IMAGES_DIR_NAME =  PROCESSED_DATA_FOLDER /"generated_svg_images"
    SVG_IMAGE_NAMES_FILE = PROCESSED_DATA_FOLDER / "corresponding_images.txt"
    FINAL_FORMULAS = PROCESSED_DATA_FOLDER / "final_formulas.txt"


    HARVARD_DIR = "DataPipes/harvardnlp_im2markup"



    FILTER_OUT_WORDS = ['%', r'\\label', r'\\cite', r'\\ref', r'\\pageref', r'\\footnote', r'\\ope', r'\\ope', r'\\qquadj' , r'\\Bar', r'\\D', r'\\wt', r'\\ww' ]

    metadata={
        'urls': [
            "http://www.cs.cornell.edu/projects/kddcup/download/hep-th-1992.tar.gz",
            "http://www.cs.cornell.edu/projects/kddcup/download/hep-th-1993.tar.gz",
            "http://www.cs.cornell.edu/projects/kddcup/download/hep-th-1994.tar.gz",
            "http://www.cs.cornell.edu/projects/kddcup/download/hep-th-1995.tar.gz",
            "http://www.cs.cornell.edu/projects/kddcup/download/hep-th-1996.tar.gz",
            "http://www.cs.cornell.edu/projects/kddcup/download/hep-th-1997.tar.gz",
            "http://www.cs.cornell.edu/projects/kddcup/download/hep-th-1998.tar.gz",
            "http://www.cs.cornell.edu/projects/kddcup/download/hep-th-1999.tar.gz",
            "http://www.cs.cornell.edu/projects/kddcup/download/hep-th-2000.tar.gz",
            "http://www.cs.cornell.edu/projects/kddcup/download/hep-th-2001.tar.gz",
            "http://www.cs.cornell.edu/projects/kddcup/download/hep-th-2002.tar.gz",
            "http://www.cs.cornell.edu/projects/kddcup/download/hep-th-2003.tar.gz"
        ]
    }
    normalizing_script_command = f"python {PREPROCESS_FORMULAS_SCRIPT_PATH} --mode normalize --input-file {NORMALIZED_FORMULAS_DIR}/formulas.txt --output-file {NORMALIZED_FORMULAS_DIR}/formulas.norm.txt"


    svg_generation_script_command =  f"python tex_to_svg.py {NORMALIZED_FORMULAS_DIR}/formulas.norm.filtered.txt {GENERATED_SVG_IMAGES_DIR_NAME}"


    png_generation_script_command =  f"python svg_to_png.py {PROCESSED_DATA_FOLDER}/corresponding_svg_images.txt {GENERATED_PNG_DIR_NAME}"