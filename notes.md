On making seams:

Using https://learn.microsoft.com/en-us/halo-master-chief-collection/h3/bsp/bsphome and https://c20.reclaimers.net/h3/guides/map-making/level-creation/blender-level-modeling/blender-level-creation-additional-info/#seams (sample files at the top of the page).

When I do the tutorial above manually (using ravine.scenario), everything works by just:

Calling `tool structure` on the exported .ASS files, calling `tool structure-seam` on the level directory, then calling `tool structure` again on the files to reimport.

Biggest issue is that for whatever reason, my geometry creates a "4 open edges" error, whereas using entirely different geometry (in a different blender file) just generates the "unmatched seam" error.

I've got it!!! It's the name of the BSP that needs to be in the seam material.