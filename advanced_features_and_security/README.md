# Advanced Features and Security Project

## Managing Permissions and Groups in Django

This project demonstrates the implementation of custom user models, groups, and permissions to control access to different parts of the application.

### Custom Permissions

Custom permissions have been added to the `users.CustomUser` model in `users/models.py`. These permissions are:
- `can_view`: Allows a user to view content.
- `can_create`: Allows a user to create new content.
- `can_edit`: Allows a user to edit existing content.
- `can_delete`: Allows a user to delete content.

### Groups and Permission Assignment

The following groups can be created in the Django admin site to manage user roles and permissions:

1.  **Viewers**: This group is assigned the `can_view` permission. Users in this group can only access the view content page.
2.  **Editors**: This group is assigned the `can_create` and `can_edit` permissions. They can create and edit content but cannot delete it.
3.  **Admins**: This group is typically a superuser or a group with all custom permissions (`can_view`, `can_create`, `can_edit`, and `can_delete`).

### Enforcing Permissions in Views

Permissions are enforced using Django's `@permission_required` decorator in the `users/views.py` file. Each view that performs a specific action (view, create, edit, delete) checks if the user has the corresponding permission before allowing access. This ensures secure access control based on user roles.

For example, the `edit_content` view is protected by the decorator: `@permission_required('users.can_edit', raise_exception=True)`.
