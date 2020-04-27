<?php

use Doctrine\ORM\EntityManager;
use Doctrine\ORM\Tools\Console\ConsoleRunner;

/**
 * @var Container $container
 */
require_once "./bootstrap.php";

return ConsoleRunner::createHelperSet($container[EntityManager::class]);