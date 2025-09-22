from db.database import SessionLocal, Base
from models.story import Story, StoryNode


class StoryGenerator:
	@classmethod
	def generate_story(cls, db, session_id: str, theme: str) -> Story:
		"""Create a minimal story with a single root node for testing."""
		story = Story(title=f"Story: {theme}", session_id=session_id)
		db.add(story)
		db.commit()
		db.refresh(story)

		root_node = StoryNode(
			story_id=story.id,
			content=f"This is the beginning of a story about {theme}.",
			is_root=True,
			is_ending=False,
			is_winning_ending=False,
			options=[],
		)
		db.add(root_node)
		db.commit()
		db.refresh(root_node)

		return story

