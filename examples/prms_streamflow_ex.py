"""Interact with the PRMSStreamflow BMI through Python."""

import os
import numpy as np
from pymt_prms_streamflow import PRMSStreamflow


run_dir = '../meta/PRMSStreamflow'
config_file = 'control.default'


# Instantiate a model and get its name.
m = PRMSStreamflow()
print(m.get_component_name())

# Initialize the model.
os.chdir(run_dir)
m.initialize(config_file)
print(config_file)

# List the model's exchange items.
print('Number of input vars:', m.get_input_item_count())
for var in m.get_input_var_names():
    print(' - {}'.format(var))
print('Number of output vars:', m.get_output_item_count())
for var in m.get_output_var_names():
    print(' - {}'.format(var))

# Get variable info.
# var_name = 'seg_outflow'
# var_name = 'flow_out'
var_name = 'hru_outflow'
print('Variable {}'.format(var_name))
print(' - variable type:', m.get_var_type(var_name))
print(' - units:', m.get_var_units(var_name))
print(' - itemsize:', m.get_var_itemsize(var_name))
print(' - nbytes:', m.get_var_nbytes(var_name))
print(' - location:', m.get_var_location(var_name))

# Get grid info for variable.
grid_id = m.get_var_grid(var_name)
print(' - grid id:', grid_id)
print(' - grid type:', m.get_grid_type(grid_id))
grid_rank = m.get_grid_rank(grid_id)
print(' - rank:', grid_rank)
grid_size = m.get_grid_size(grid_id)
print(' - size:', grid_size)
grid_shape = np.empty(grid_rank, dtype=np.int32)
try:
    m.get_grid_shape(grid_id, grid_shape)
except RuntimeError:
    print(' - shape: n/a')
else:
    print(' - shape:', grid_shape)
grid_spacing = np.empty(grid_rank, dtype=np.float64)
try:
    m.get_grid_spacing(grid_id, grid_spacing)
except RuntimeError:
    print(' - spacing: n/a')
else:
    print(' - spacing:', grid_spacing)
grid_origin = np.empty(grid_rank, dtype=np.float64)
try:
    m.get_grid_origin(grid_id, grid_origin)
except RuntimeError:
    print(' - origin: n/a')
else:
    print(' - origin:', grid_origin)
grid_x = np.empty(grid_size, dtype=np.float64)
m.get_grid_x(grid_id, grid_x)
print(' - x:', grid_x)
grid_y = np.empty(grid_size, dtype=np.float64)
m.get_grid_y(grid_id, grid_y)
print(' - y:', grid_y)
grid_z = np.empty(grid_size, dtype=np.float64)
m.get_grid_z(grid_id, grid_z)
print(' - z:', grid_z)

# Get time information from the model.
print('Start time:', m.get_start_time())
print('End time:', m.get_end_time())
print('Current time:', m.get_current_time())
print('Time step:', m.get_time_step())
print('Time units:', m.get_time_units())

# Advance the model by one time step.
print('Advance model by a single time step...')
m.update()
print(' - new time:', m.get_current_time())

# Advance the model until a later time.
print('Advance model to a later time...')
m.update_until(5.0)
print(' - new time:', m.get_current_time())

# Get the variable values.
print('Get values of {}...'.format(var_name))
val = np.empty(grid_size, dtype=m.get_var_type(var_name))
m.get_value(var_name, val)
print(' - values at time {}:'.format(m.get_current_time()))
print(val)

# Get a reference to the variable and check that it updates.
if m.get_grid_type(grid_id) != 'scalar':
    ref = m.get_value_ptr(var_name)
    for _ in range(3):
        print(' - values (by ref) at time {}:'.format(m.get_current_time()))
        print(ref)
        m.update()

# Set new variable values.
if var_name not in m.get_output_var_names():
    print('Set values of {}...'.format(var_name))
    new = np.arange(grid_size, dtype=m.get_var_type(var_name))
    print(' - values to set:', new)
    m.set_value(var_name, new)
    print(' - check that values were set:', ref)

# Finalize the model.
m.finalize()
print('Done.')
