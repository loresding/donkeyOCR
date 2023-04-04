import os

class Settings:
    ROOT = os.path.dirname(os.path.abspath(__file__))
    CACHE_PATH = os.path.join(ROOT, "cache")

    CNOCR_MODEL_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "core/models")

    BOX_COLORS = [(82, 85, 255), (255, 130, 80), (240, 70, 255), (255, 255, 19), (30, 255, 30)]


