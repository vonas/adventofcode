from test.helper import use_example, skip


class part_1:
  @use_example(1)
  def test_example_1(self, problem):
    assert problem.solve_1() == 8

  @use_example(2)
  def test_example_1(self, problem):
    assert problem.solve_1() == 2

  def test_solution(self, problem):
    assert problem.solve_1() == 165


@skip
class part_2:
  def test_solution(self, problem):
    assert problem.solve_2() == 0000
