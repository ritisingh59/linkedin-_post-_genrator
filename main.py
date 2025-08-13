import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

def main():
    st.title("LinkedIn Post Generator")

    fs = FewShotPosts()

    col1, col2, col3 = st.columns(3)

    with col1:
        selected_tag = st.selectbox("Select Tag", options=fs.get_tags())

    with col2:
        selected_language = st.selectbox("Select Language", options=fs.df["language"].unique())

    with col3:
        selected_length = st.selectbox("Select Length", options=["Short", "Medium", "Long"])

    if st.button("Generate Posts"):
        posts = fs.get_filtered_posts(selected_length, selected_language, selected_tag)
        if posts:
            for i, post in enumerate(posts):
                st.markdown(f"### Post {i+1}")
                st.write(post.get("Text", "No content available."))
                st.markdown("---")
        else:
            st.warning("No posts found for selected filters.")

if __name__ == "__main__":
    main()
