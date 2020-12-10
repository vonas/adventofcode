from test.helper import use_example


class part_1:
  @use_example(1)
  def test_example_1(self, problem):
    assert problem.solve()[0] == 2

  def test_solution(self, problem):
    assert problem.solve()[0] == 216


class part_2:
  @use_example(2)
  def test_example_2(self, problem):
    assert problem.solve()[1] == 0

  @use_example(3)
  def test_example_3(self, problem):
    assert problem.solve()[1] == 4

  def test_solution(self, problem):
    assert problem.solve()[1] == 150
