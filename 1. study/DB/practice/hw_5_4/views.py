# articles/views.py

def likes(request, article_pk):
	article = Article.objects.get(pk=article_pk)
	if article.__(a)__.filter(pk=request.user.pk).__(b)__():
		article.like_users.remove(request.user)
	else:
		article.like_users.__(c)__(request.user)

	return redirect('articles:index')


(a) like_users
(b) exists
(c) add