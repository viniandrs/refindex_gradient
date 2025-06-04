import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Refindex Gradient Experiment")
    parser.add_argument("name", type=str, help="Name of the experiment")
    parser.add_argument("n_layers", type=int, help="Number of layers in the medium")
    parser.add_argument("n_0", type=float, default=1.3, help="Refractive index of the first layer")
    parser.add_argument("n_f", type=float, default=1.5, help="Refractive index of the last layer")
    parser.add_argument("y_beam", type=float, default=25.0, help="Initial y position of the light beam in cm")
    
    return parser.parse_args()

def main(args):
    container = Container(width=40, height=25)
    medium = Medium(
        n_0=1.0, 
        n_f=1.5, 
        n_layers=15, 
        color='blue'
    )

    geometry = Geometry(container, medium)
    geometry.render_container()
    geometry.render_medium()

if __name__ == "__main__":
    try:
        args = parse_args()
        main(args)
    except:
        print('Try $python <script_name> "Hello" 123 --enable')