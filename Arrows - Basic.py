
# coding: utf-8

# In[10]:


p = arrow((0,1),(2,3))[0]
type (p)
p


# In[13]:


d = arrow((1,1),(5,5)).get_minmax_data()
d['xmin']


# In[14]:


d['xmax']


# In[16]:


a = arrow((0,0),(1,1))[0].plot3d()
a.jmol_repr(a.testing_render_params())[0]


# In[17]:


a = arrow((0,0),(1,1))[0].plot3d(3)
a.jmol_repr(a.testing_render_params())[0][0]


# In[18]:


a = arrow((0,0),(1,1))[0].plot3d(3,4)
a.jmol_repr(a.testing_render_params())[0]


# In[19]:


from sage.plot.arrow import CurveArrow


# In[25]:


b = CurveArrow(path = [[(0,0),(0.5,0.5),(1,0)],[(0.5,1),(0,0)]], options = {})
b


# In[27]:


d = b.get_minmax_data()
d['xmin']


# In[28]:


d['xmax']


# In[29]:


arrow((0,0),(1,1))


# In[30]:


arrow((0,0,1),(1,1,1))


# In[32]:


from sage.plot.bezier_path import BezierPath


# In[33]:


BezierPath([[(0,0),(0.5,0.5),(1,0)],[(0.5,1),(0,0)]],{'linestyle': 'dashed'})


# In[41]:


bezier_path([[(0,0),(.5,.5),(1,0)],[(.5,1),(0,0)]], linestyle="dashed")


# In[45]:


b = bezier_path([[(0,0),(.5,.5),(1,0)],[(.5,1),(0,0)]], linestyle="dashed")
d = b.get_minmax_data()
d['xmin']


# In[46]:


d['xmax']


# In[47]:


b = bezier_path([[(0,0),(0,1),(1,0)]])
A = b.plot3d()
B = b.plot3d(z=2)
A + B


# In[48]:


bezier3d([[(0,0,0),(1,0,0),(0,1,0),(0,1,1)]])

