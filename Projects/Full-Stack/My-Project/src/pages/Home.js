import React from 'react';
import RecipeSearchForm from '../components/RecipeSearchForm';
import RecipeList from '../components/RecipeList';
import Pagination from '../components/Pagination';

const Home = () => {
  return (
    <div>
      <section>
        <RecipeSearchForm />
      </section>
      <section>
        <RecipeList />
      </section>
      <section>
        <Pagination />
      </section>
    </div>
  );
};

export default Home;
