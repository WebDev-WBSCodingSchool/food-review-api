-- USERS TABLE
CREATE TABLE public.users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

-- RESTAURANTS TABLE
CREATE TABLE public.restaurants (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    owner_id INTEGER NOT NULL,
    CONSTRAINT restaurants_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES public.users(id)
);

-- REVIEWS TABLE
CREATE TABLE public.reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    restaurant_id INTEGER NOT NULL,
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    comment TEXT,
    CONSTRAINT reviews_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id),
    CONSTRAINT reviews_restaurant_id_fkey FOREIGN KEY (restaurant_id) REFERENCES public.restaurants(id)
);

-- Insert sample users
INSERT INTO public.users (username, email, password) VALUES
('alice', 'alice@example.com', 'password123'),
('bob', 'bob@example.com', 'securepass'),
('carol', 'carol@example.com', 'qwerty456');

-- Insert sample restaurants
INSERT INTO public.restaurants (name, description, owner_id) VALUES
('Pasta Palace', 'Authentic Italian pasta and more.', 1),
('Sushi Central', 'Fresh sushi with a modern twist.', 2),
('Taco Town', 'Street-style tacos and tequila.', 1);

-- Insert sample reviews
INSERT INTO public.reviews (user_id, restaurant_id, rating, comment) VALUES
(2, 1, 5, 'Amazing pasta! Will come back for sure.'),
(3, 1, 4, 'Great food but service was a bit slow.'),
(1, 2, 5, 'Best sushi I’ve had in a while!'),
(3, 2, 3, 'Sushi was decent, but a bit overpriced.'),
(2, 3, 4, 'Tacos were delicious, especially the carnitas.');
