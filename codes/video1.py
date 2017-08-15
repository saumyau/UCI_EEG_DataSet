import os
import seaborn

example_vid = os.path.join('assets', 'some_video.mp4')
example_points = [(100, 100, 25), (112, 92, 67), (17, 100, 36)]

img_heatmapper = Heatmapper()
video_heatmapper = VideoHeatmapper(img_heatmapper)

heatmap_video = video_heatmapper.heatmap_on_video_path(
    video_path=example_vid,
    points=example_points
)

heatmap_video.write_videofile('out.mp4', bitrate="5000k", fps=24)
