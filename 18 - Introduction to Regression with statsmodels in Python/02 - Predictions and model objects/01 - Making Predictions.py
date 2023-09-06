# Import numpy with alias np
import numpy as np
import pandas as pd

# Create the explanatory_data
explanatory_data = pd.DataFrame({'n_convenience': np.arange(11)})

# Print it
print(explanatory_data)

# Import numpy with alias np
import numpy as np
import pandas as pd

# Create explanatory_data
explanatory_data = pd.DataFrame({'n_convenience': np.arange(0, 11)})

# Use mdl_price_vs_conv to predict with explanatory_data, call it price_twd_msq
price_twd_msq = mdl_price_vs_conv.predict(explanatory_data)

# Print it
print(price_twd_msq)
