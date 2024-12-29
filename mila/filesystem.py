from .constants import *
import os
import toml

class Theme():
    def __init__(self, *args: dict[dict, dict], **kwargs):
        """
        Theme class to represent a theme. can take a dictionary of parameters or keyword arguments from `mila.toml` file
        
        Attributes
        ----------

        `name` : str
            name of the theme. `Default`: None
        """
    
        if args and isinstance(args[0], dict[dict]):
            params: dict[dict] = args[0]
            # Remap nested dictionary to a flat dictionary
            params = {k: v for d in args[0].values() for k, v in d.items()}
        else:
            params = kwargs

        self.name = params.get('name', None)
        self.path = os.path.join(THEMES_DIR, self.name)

    def to_dict(self):
        return {
            'general': {
                'name': self.name,
            },
        }

    def save(self):
        """
        Save the theme to a toml file
        """
        os.makedirs(self.path, exist_ok=True)
        with open(os.path.join(self.path, THEME_DATA_FILE_NAME), 'w') as f:
            toml.dump(self.to_dict(), f)
