from baccala import *
import pygame

pygame.init()

display = pygame.display.set_mode((800, 600))
surface = pygame.Surface((800, 600))
clock = pygame.time.Clock()

projection = BaccalaMatrix(BaccalaMatrixPresets.ORTHO3D)

rot_matrix_x = BaccalaRotationMatrix(BaccalaRotationMatrixPresets.X)
rot_matrix_y = BaccalaRotationMatrix(BaccalaRotationMatrixPresets.Y)
rot_matrix_z = BaccalaRotationMatrix(BaccalaRotationMatrixPresets.Y)

cube = BACC_PRESET_CUBE()

angle = 0

while True:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			exit()

	angle += 1
	angle %= 360

	surface.fill((0, 0, 0))

	Positions = []
	for vertex in cube.BACC_VERTEX_LIST:
		new_vertex = [vertex[0] * cube.BACC_WIDTH, vertex[1] * cube.BACC_HEIGHT, vertex[2] * cube.BACC_DEPTH]
		new_vertex = rot_matrix_x.run(angle, new_vertex)
		new_vertex = rot_matrix_y.run(angle, new_vertex)

		x, y = projection.run(*new_vertex)

		pos = [400 + int(x), 300 + int(y)]

		Positions += [pos]

	for source, destination in cube.BACC_WIREFRAME_ORDER:
		pygame.draw.line(surface, (255, 255, 255), Positions[source], Positions[destination])

	display.blit(surface, (0, 0))
	pygame.display.update()
	clock.tick(60)
