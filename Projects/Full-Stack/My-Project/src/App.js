import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Layout from './components/NavBar';

// pages
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';
import Login from './pages/Login';
import RecipeDetails from './pages/RecipeDetails';
import RecipeList from './pages/RecipeList';
import SignUp from './pages/SignUp';
import NotFound from './pages/NotFound';

// redux
import { Provider } from 'react-redux';
import store from './store';

const App = () => {
  <Provider store={store}>
    <Router>
      <Layout>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/about" component={About} />
          <Route exact path="/contact" component={Contact} />
          <Route exact path="/recipe/:id" component={RecipeDetails} />
          <Route exact path="/recipe" component={RecipeList} />
          <Route exact path="/signup" component={SignUp} />
          <Route exact path="/login" component={Login} />
          <Route component={NotFound} />
        </Switch>
      </Layout>
    </Router>
  </Provider>;
};

export default App;
