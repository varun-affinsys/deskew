import os
import pytest
from skimage import io
from skimage.color import rgb2gray
from deskew import determine_skew


@pytest.mark.parametrize('image,expected_angle', [
    ('1', pytest.approx(-1.375, abs=0.37)),
    ('2', pytest.approx(-2.185, abs=0.18)),
    ('3', pytest.approx(-6.250, abs=0.22)),
    ('4', pytest.approx(7.095, abs=0.1)),
    ('5', pytest.approx(3.410, abs=0.7)),
    ('6', pytest.approx(-2.810, abs=0.21)),
    ('7', pytest.approx(3.395, abs=0.7)),
])
def test_deskew(image, expected_angle):
    root_folder = 'results/{}'.format(image)
    if not os.path.exists(root_folder):
        os.makedirs(root_folder)

    image = io.imread(os.path.join(os.path.dirname(__file__), 'deskew-{}.png'.format(image)))
    grayscale = rgb2gray(image)
    angle = determine_skew(grayscale)
    print(angle - expected_angle.expected)
    assert angle == expected_angle