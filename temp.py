import os

def create_project_structure(base_dir):
    directories = [
        base_dir,
        os.path.join(base_dir, 'flp'),
        os.path.join(base_dir, 'flp', 'subpackage'),
        os.path.join(base_dir, 'tests'),
        os.path.join(base_dir, 'docs'),
        os.path.join(base_dir, 'data')
    ]
    
    files = [
        os.path.join(base_dir, 'README.md'),
        os.path.join(base_dir, 'setup.py'),
        os.path.join(base_dir, 'requirements.txt'),
        os.path.join(base_dir, '.gitignore'),
        os.path.join(base_dir, 'flp', '__init__.py'),
        os.path.join(base_dir, 'flp', 'main.py'),
        os.path.join(base_dir, 'flp', 'module1.py'),
        os.path.join(base_dir, 'flp', 'module2.py'),
        os.path.join(base_dir, 'flp', 'subpackage', '__init__.py'),
        os.path.join(base_dir, 'flp', 'subpackage', 'submodule.py'),
        os.path.join(base_dir, 'tests', '__init__.py'),
        os.path.join(base_dir, 'tests', 'test_main.py'),
        os.path.join(base_dir, 'tests', 'test_module1.py'),
        os.path.join(base_dir, 'tests', 'test_module2.py'),
        os.path.join(base_dir, 'docs', 'index.md'),
        os.path.join(base_dir, 'data', 'data1.csv'),
        os.path.join(base_dir, 'data', 'data2.csv'),
        os.path.join(base_dir, 'data', 'data1.xlsx'),
        os.path.join(base_dir, 'data', 'data2.xlsx')
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    for file in files:
        with open(file, 'w') as f:
            pass
    
    # Write .gitignore content
    gitignore_content = """# Ignore all files in the data folder
data/*

# Do not ignore files that start with sample_data
!data/sample_data*
"""
    with open(os.path.join(base_dir, '.gitignore'), 'w') as f:
        f.write(gitignore_content)

if __name__ == "__main__":
    create_project_structure('.')
