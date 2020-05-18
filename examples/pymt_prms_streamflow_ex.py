"""Run the PRMSStreamflow component in pymt."""

import numpy as np
from pymt.models import PRMSStreamflow


run_dir = '../meta/PRMSStreamflow'
config_file = 'control.default'


# Instantiate the component and get its name.
m = PRMSStreamflow()
print(m.name)

# Initialize the model. (Skipping setup step)
print(run_dir)
print(config_file)
m.initialize(config_file, run_dir)

# List the model's exchange items.
print('Number of input vars:', len(m.input_var_names))
for var in m.input_var_names:
    print(' - {}'.format(var))
print('Number of output vars:', len(m.output_var_names))
for var in m.output_var_names:
    print(' - {}'.format(var))

# Get variable info.
var_name = 'hru_outflow'
print('Variable {}'.format(var_name))
print(' - variable type:', m.var_type(var_name))
print(' - units:', m.var_units(var_name))
print(' - itemsize:', m.var_itemsize(var_name))
print(' - nbytes:', m.var_nbytes(var_name))
print(' - location:', m.var_location(var_name))

# Get grid info for variable.
grid_id = m.var_grid(var_name)
print(' - grid id:', grid_id)
print(' - grid type:', m.grid_type(grid_id))
print(' - rank:', m.grid_ndim(grid_id))

if m.grid_type(grid_id) == 'rectilinear':
    print(' - size:', m.grid_node_count(grid_id))
    print(' - shape:', m.grid_shape(grid_id))

print(' - x:', m.grid_x(grid_id))
print(' - y:', m.grid_y(grid_id))
print(' - z:', m.grid_z(grid_id))

if m.grid_type(grid_id) != 'rectilinear':
    print(' - node count:', m.grid_node_count(grid_id))
    print(' - face count:', m.grid_face_count(grid_id))
    print(' - edge count:', m.grid_edge_count(grid_id))

# Get time information from the model.
print('Start time:', m.start_time)
print('End time:', m.end_time)
print('Current time:', m.time)
print('Time step:', m.time_step)
print('Time units:', m.time_units)

# Advance the model by one time step.
m.update()
print('Update: current time:', m.time)

# Advance the model until a later time.
m.update_until(5.0)
print('Update: current time:', m.time)

# Get the variable values.
print('Get values of {}...'.format(var_name))
val = m.var[var_name].data
# val = m.get_value(var_name)
print(' - values at time {}:'.format(m.time))
print(val)

# Get a reference to the variable and check that it updates.
if m.grid_type(grid_id) != 'scalar':
    ref = m.get_value_ptr(var_name)
    for _ in range(3):
        print(' - values (by ref) at time {}:'.format(m.time))
        print(ref)
        m.update()

# Set new variable values.
if var_name not in m.output_var_names:
    new = np.arange(m.grid_node_count(grid_id), dtype=m.var_type(var_name))
    m.set_value(var_name, new)
    print('Set values of {}...'.format(var_name))
    print(' - values to set:', new)
    print(' - check that values were set:', ref)

# Finalize the model.
m.finalize()
print('Done.')
