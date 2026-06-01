from fastapi import FastAPI,HTTPException

app = FastAPI()

#dummy posts
text_posts = {
    1: {"title": "New Posts", "content": "Cool new posts"},
    2: {"title": "Morning Workout", "content": "Completed a 30 minute workout session"},
    3: {"title": "Book Recommendation", "content": "Just finished reading an amazing science fiction novel"},
    4: {"title": "Travel Plans", "content": "Planning a weekend trip to the mountains"},
    5: {"title": "Learning FastAPI", "content": "Built my first REST API endpoint today"},
    6: {"title": "Coffee Break", "content": "Trying a new coffee blend from a local cafe"},
    7: {"title": "Photography Tips", "content": "Experimenting with portrait lighting techniques"},
    8: {"title": "Movie Night", "content": "Watching a classic thriller this evening"},
    9: {"title": "Coding Progress", "content": "Successfully implemented user authentication"},
    10: {"title": "Healthy Recipes", "content": "Made a homemade vegetable pasta for dinner"}
}

@app.get('/posts')
def get_all_post(limit : int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get('/posts/{id}')
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail='Post not found')
    return text_posts.get(id)

