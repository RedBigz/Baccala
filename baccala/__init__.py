import pygame
from math import *
from copy import deepcopy

pygame.init()

class BaccalaInstance:
	def BACC_initialize(self, surfacetype, RES):
		self.BACC_scene = None

		if surfacetype.lower() == "pygame":
			self.BACC_st = "pg"
			self.BACC_s = pygame.Surface(RES)


	def BACC_SCENE_update(self, scene):
		self.BACC_scene = scene


	def BACC_render(self):
		if self.BACC_scene is None:
			return False
		else:

			return True

class BaccalaMatrixPresets:
	ORTHO3D = [
		[1, 0, 0],
		[0, 1, 0]
	]

class BaccalaMatrix:
	def __init__(self, matrix):
		self.matrix = matrix

	def run(self, *args):
		res = []
		for y in self.matrix:
			a = 0
			for i in [y[i] * args[i] for i in range(len(y))]:
				a += i

			res += [a]

		return res

class BaccalaRotationMatrixPresets:
	X = "[[cos(a), 0, -sin(a)], [0, 1, 0], [sin(a), 0, cos(a)]]"
	Y = "[[1, 0, 0], [0, cos(a), -sin(a)], [0, sin(a), cos(a)]]"
	Z = "[[0, cos(a), -sin(a)], [0, sin(a), cos(a)], [0, 0, 1]]"

class BaccalaRotationMatrix(BaccalaMatrix):
	def run(self, angle, xyz):
		a = radians(angle)
		self.b = deepcopy(self.matrix)
		self.matrix = eval(self.matrix)
		r = super().run(*xyz)
		self.matrix = deepcopy(self.b)
		return r


class BACC_MODEL_BASIC:
	def BACC_INIT_VERTICES(self, vertices): self.BACC_VERTEX_LIST = vertices

	def BACC_INIT_WIREFRAME(self, wf):
		self.BACC_WIREFRAME_ORDER = wf

	def BACC_INIT(self, vertices, wireframe = None, w = 100, h = 100, d = 100):
		self.BACC_INIT_VERTICES(vertices)
		self.BACC_WIDTH, self.BACC_HEIGHT, self.BACC_DEPTH = w, h, d
		self.BACC_INIT_WIREFRAME(wireframe)

class BACC_PRESET_SQUARE(BACC_MODEL_BASIC):
	def __init__(self):
		super().BACC_INIT(
			vertices = [
				(-1, -1, 0),
				(1, -1, 0),
				(1, 1, 0),
				(-1, 1, 0),
			],
			wireframe = [
				#0, 1, 2, 3, 0
			],
			d = 0
		)

class BACC_PRESET_CUBE(BACC_MODEL_BASIC):
	def __init__(self):
		super().BACC_INIT(
			vertices = [
				(-1, -1, -1),
				(1, -1, -1),
				(1, 1, -1),
				(-1, 1, -1),
				(-1, -1, 1),
				(1, -1, 1),
				(1, 1, 1),
				(-1, 1, 1),
			],
			wireframe = [
				(0, 1),
				(1, 2),
				(2, 3),
				(3, 0),
				(0, 4),
				(1, 5),
				(2, 6),
				(3, 7),
				(4, 5),
				(5, 6),
				(6, 7),
				(7, 4),
			]
		)