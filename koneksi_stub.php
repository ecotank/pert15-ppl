<?php
/**
 * Stub Module for Database Connection and User Fixtures
 * Used for isolation testing of Login and Register modules.
 */

class DatabaseStub {
    private static $mockUsers = [
        [
            'id' => 1,
            'name' => 'User Test Stub',
            'username' => 'stubuser',
            'email' => 'stubuser@example.com',
            'password' => '$2y$10$D9yc9Mt0t8niCNO9di8ejOUPib46suwHghqFnJRKQJ3Z6uwRDxfw.' // pass: password123
        ]
    ];

    public static function getMockUsers() {
        return self::$mockUsers;
    }

    public static function addMockUser($name, $username, $email, $password) {
        self::$mockUsers[] = [
            'id' => count(self::$mockUsers) + 1,
            'name' => $name,
            'username' => $username,
            'email' => $email,
            'password' => password_hash($password, PASSWORD_DEFAULT)
        ];
        return true;
    }
}
?>
