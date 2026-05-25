import sys
import re


def main(args):

    if not len(args) == 2 or not args[1].endswith('.cif'):
        print("Usage: python export_table_from_cif.py <input_file.cif>")
        sys.exit(1)
        
    reg_s = re.compile(r'\s+')

    with open(args[1], 'r') as f:
        cif_lines = f.readlines()

    cif_dict = {}
    for line in cif_lines:
        line = reg_s.split(line)        # Split by whitespace
        line = [ x for x in line if x ] # Remove empty strings
        if len(line) == 2 and line[0].startswith('_'):
            cif_dict[line[0]] = line[1]


    # Extract the desired values, can be extended to include more fields as needed
    chemical_formula_sum = cif_dict.get('_chemical_formula_sum',               'N/A')
    space_group_name     = cif_dict.get('_symmetry_space_group_name_H-M',      'N/A')
    cell_length_a        = cif_dict.get('_cell_length_a',                      'N/A')
    cell_length_b        = cif_dict.get('_cell_length_b',                      'N/A')
    cell_length_c        = cif_dict.get('_cell_length_c',                      'N/A')
    cell_angle_alpha     = cif_dict.get('_cell_angle_alpha',                   'N/A')
    cell_angle_beta      = cif_dict.get('_cell_angle_beta',                    'N/A')
    cell_angle_gamma     = cif_dict.get('_cell_angle_gamma',                   'N/A')
    cell_volume          = cif_dict.get('_cell_volume',                        'N/A')
    device_type          = cif_dict.get('_diffrn_measurement_device_type',     'N/A')
    detector             = cif_dict.get('_diffrn_detector',                    'N/A')
    wavelength           = cif_dict.get('_diffrn_radiation_wavelength',        'N/A')
    tth_refine_min       = cif_dict.get('_pd_proc_2theta_range_min',           'N/A')
    tth_refine_max       = cif_dict.get('_pd_proc_2theta_range_max',           'N/A')
    Rwp                  = cif_dict.get('_pd_proc_ls_prof_wR_factor',          'N/A')
    Rexp                 = cif_dict.get('_pd_proc_ls_prof_wR_expected',        'N/A')
    Gof                  = cif_dict.get('_refine_ls_goodness_of_fit_all',      'N/A')

    with open(args[1].replace('.cif', '_export_table.txt'), 'wt') as f:
        f.write(f"Formula\t{chemical_formula_sum}\n")
        f.write(f"Space Group\t{space_group_name}\n")
        f.write(f"a\t{cell_length_a}\n")
        f.write(f"b\t{cell_length_b}\n")
        f.write(f"c\t{cell_length_c}\n")
        f.write(f"alpha\t{cell_angle_alpha}\n")
        f.write(f"beta\t{cell_angle_beta}\n")
        f.write(f"gamma\t{cell_angle_gamma}\n")
        f.write(f"Cell Volume\t{cell_volume}\n")
        f.write(f"Device\t{device_type}\n")
        f.write(f"Detector\t{detector}\n")
        f.write(f"Wavelength\t{wavelength}\n")
        f.write(f"Refinement 2Theta\t{tth_refine_min}-{tth_refine_max}\n")
        f.write(r"Rwp\Rexp\Gof" f"\t{Rwp}\\{Rexp}\\{Gof}\n")

if __name__ == "__main__":
    main(sys.argv)
