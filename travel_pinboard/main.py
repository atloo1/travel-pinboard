from numbers import Number
from typing import Tuple, Union

import pandas as pd
from PIL import Image


def get_tip_details_set():
    """parse spreadsheet for pins' (x, y, θ)"""
    df = pd.read_csv('input/pinboard.tsv', sep='\t', na_values='-')
    cols = ['x', 'y', 'θ']
    mask = df[cols].notna().all(axis=1)
    df = df[cols].loc[mask].astype(int)
    tip_details_set = set(df.itertuples(index=False, name=None))
    return tip_details_set


def heading_to_theta(heading: Union[float, int]) -> Union[float, int]:
    """
    convert compass heading (°) to an equivalent for PIL.Image.rotate

    equivalent to piecewise
    f(θ) = -θ + 90 [0 ≤ θ ≤ 90] &
    f(θ) = -θ + 450 [90 < θ ≤ 360]
    """
    if not (0 <= heading <= 360):
        raise ValueError(f'{heading}° not in range [0, 360]')
    if heading <= 90:
        heading += 360
    theta = 450 - heading
    return theta


def get_coordinates(tip_x: int, tip_y: int, heading: Number) -> Tuple[int, int]:
    """
    convert tip coordinates to an equivalent for PIL.Image.paste

    hard coded for 11x26 arrow b/c 45° rotation resizes image, complicating math
    """
    top_left_x = tip_x
    top_left_y = tip_y
    if heading == 45:
        top_left_x -= 23
        top_left_y -= 4
    elif heading == 135:
        top_left_x -= 23
        top_left_y -= 22
    elif heading == 225:
        top_left_x -= 5
        top_left_y -= 22
    elif heading == 315:
        top_left_x -= 5
        top_left_y -= 4
    else:
        raise NotImplementedError(f'{heading}° rotation not implemented')
    return top_left_x, top_left_y


def main():
    """make & save pinboard"""
    map = Image.open('input/map.png')
    pin = Image.open('input/pin.png')
    tip_details_set = get_tip_details_set()

    for tip_x, tip_y, heading in tip_details_set:
        theta = heading_to_theta(heading)
        rotated_pin = pin.rotate(theta, resample=Image.BICUBIC, expand=True)
        coordinates = get_coordinates(tip_x, tip_y, heading)
        map.paste(rotated_pin, coordinates, rotated_pin)

    map.save('output/pinboard.png')
    map.show()


if __name__ == '__main__':
    main()
