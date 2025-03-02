import unittest
from app.models import CustomEnv, train_reinforcement_learning_model

class TestModels(unittest.TestCase):
    def test_custom_env_reset(self):
        env = CustomEnv()
        state = env.reset()
        self.assertEqual(state, 0)

    def test_custom_env_step(self):
        env = CustomEnv()
        env.reset()
        state, reward, done, _ = env.step(1)
        self.assertEqual(state, 1)
        self.assertEqual(reward, 1)
        self.assertFalse(done)

    def test_train_reinforcement_learning_model(self):
        model = train_reinforcement_learning_model()
        self.assertIsNotNone(model)

if __name__ == "__main__":
    unittest.main()